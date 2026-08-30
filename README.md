# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 444
- HTTP: 113 alive / 84 gold
- HTTPS: 64 alive / 31 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44579
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
