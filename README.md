# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 359
- HTTP: 241 alive / 84 gold
- HTTPS: 199 alive / 19 gold
- SOCKS4: 206 alive / 143 gold
- SOCKS5: 176 alive / 113 gold

## Historical pool

- Discovered: 145270
- Ever alive: 25330
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
