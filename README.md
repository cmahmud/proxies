# SyndProxy private pool

## Current pool

- Alive now: 1174
- Gold now: 556
- HTTP: 432 alive / 164 gold
- HTTPS: 290 alive / 92 gold
- SOCKS4: 232 alive / 151 gold
- SOCKS5: 220 alive / 149 gold

## Historical pool

- Discovered: 123175
- Ever alive: 18906
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
