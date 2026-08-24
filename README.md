# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 387
- HTTP: 118 alive / 64 gold
- HTTPS: 48 alive / 8 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 191 alive / 159 gold

## Historical pool

- Discovered: 177586
- Ever alive: 33324
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
