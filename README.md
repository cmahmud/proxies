# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 411
- HTTP: 211 alive / 86 gold
- HTTPS: 164 alive / 27 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 243 alive / 160 gold

## Historical pool

- Discovered: 162438
- Ever alive: 31416
- Ever gold: 1159

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
