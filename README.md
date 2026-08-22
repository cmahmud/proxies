# SyndProxy private pool

## Current pool

- Alive now: 955
- Gold now: 426
- HTTP: 275 alive / 86 gold
- HTTPS: 220 alive / 30 gold
- SOCKS4: 207 alive / 147 gold
- SOCKS5: 253 alive / 163 gold

## Historical pool

- Discovered: 162748
- Ever alive: 31537
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
