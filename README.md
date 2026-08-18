# SyndProxy private pool

## Current pool

- Alive now: 715
- Gold now: 244
- HTTP: 197 alive / 27 gold
- HTTPS: 127 alive / 9 gold
- SOCKS4: 181 alive / 106 gold
- SOCKS5: 210 alive / 102 gold

## Historical pool

- Discovered: 95258
- Ever alive: 10188
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
