# SyndProxy private pool

## Current pool

- Alive now: 1045
- Gold now: 555
- HTTP: 378 alive / 173 gold
- HTTPS: 241 alive / 91 gold
- SOCKS4: 210 alive / 144 gold
- SOCKS5: 216 alive / 147 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19161
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
