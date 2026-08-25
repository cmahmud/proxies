# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 415
- HTTP: 91 alive / 58 gold
- HTTPS: 82 alive / 19 gold
- SOCKS4: 174 alive / 164 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36167
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
