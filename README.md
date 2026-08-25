# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 414
- HTTP: 88 alive / 58 gold
- HTTPS: 83 alive / 18 gold
- SOCKS4: 170 alive / 164 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36153
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
