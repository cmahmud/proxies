# SyndProxy private pool

## Current pool

- Alive now: 850
- Gold now: 451
- HTTP: 216 alive / 106 gold
- HTTPS: 167 alive / 29 gold
- SOCKS4: 211 alive / 153 gold
- SOCKS5: 256 alive / 163 gold

## Historical pool

- Discovered: 163327
- Ever alive: 31829
- Ever gold: 1167

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
