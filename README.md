# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 406
- HTTP: 106 alive / 68 gold
- HTTPS: 181 alive / 20 gold
- SOCKS4: 174 alive / 157 gold
- SOCKS5: 188 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40598
- Ever gold: 1310

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
