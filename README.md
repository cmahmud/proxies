# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 547
- HTTP: 353 alive / 164 gold
- HTTPS: 236 alive / 91 gold
- SOCKS4: 210 alive / 146 gold
- SOCKS5: 200 alive / 146 gold

## Historical pool

- Discovered: 124825
- Ever alive: 19155
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
