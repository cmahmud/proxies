# SyndProxy private pool

## Current pool

- Alive now: 1385
- Gold now: 598
- HTTP: 502 alive / 208 gold
- HTTPS: 409 alive / 104 gold
- SOCKS4: 236 alive / 150 gold
- SOCKS5: 238 alive / 136 gold

## Historical pool

- Discovered: 140466
- Ever alive: 23718
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
