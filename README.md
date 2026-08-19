# SyndProxy private pool

## Current pool

- Alive now: 993
- Gold now: 525
- HTTP: 343 alive / 164 gold
- HTTPS: 219 alive / 90 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 203 alive / 125 gold

## Historical pool

- Discovered: 123233
- Ever alive: 19014
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
