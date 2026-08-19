# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 538
- HTTP: 427 alive / 161 gold
- HTTPS: 284 alive / 90 gold
- SOCKS4: 229 alive / 144 gold
- SOCKS5: 208 alive / 143 gold

## Historical pool

- Discovered: 123921
- Ever alive: 19152
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
