# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 416
- HTTP: 90 alive / 59 gold
- HTTPS: 91 alive / 20 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 191 alive / 174 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36173
- Ever gold: 1268

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
