# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 412
- HTTP: 350 alive / 103 gold
- HTTPS: 248 alive / 25 gold
- SOCKS4: 236 alive / 154 gold
- SOCKS5: 221 alive / 130 gold

## Historical pool

- Discovered: 160980
- Ever alive: 30832
- Ever gold: 1149

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
