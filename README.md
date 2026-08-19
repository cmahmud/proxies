# SyndProxy private pool

## Current pool

- Alive now: 1158
- Gold now: 540
- HTTP: 431 alive / 163 gold
- HTTPS: 289 alive / 89 gold
- SOCKS4: 229 alive / 145 gold
- SOCKS5: 209 alive / 143 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19145
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
