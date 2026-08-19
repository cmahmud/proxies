# SyndProxy private pool

## Current pool

- Alive now: 1109
- Gold now: 523
- HTTP: 387 alive / 154 gold
- HTTPS: 259 alive / 94 gold
- SOCKS4: 251 alive / 148 gold
- SOCKS5: 212 alive / 127 gold

## Historical pool

- Discovered: 123226
- Ever alive: 18919
- Ever gold: 730

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
