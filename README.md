# SyndProxy private pool

## Current pool

- Alive now: 865
- Gold now: 418
- HTTP: 241 alive / 91 gold
- HTTPS: 171 alive / 26 gold
- SOCKS4: 210 alive / 143 gold
- SOCKS5: 243 alive / 158 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31841
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
