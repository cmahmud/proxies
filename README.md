# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 432
- HTTP: 300 alive / 109 gold
- HTTPS: 211 alive / 28 gold
- SOCKS4: 236 alive / 153 gold
- SOCKS5: 234 alive / 142 gold

## Historical pool

- Discovered: 160020
- Ever alive: 30533
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
