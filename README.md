# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 443
- HTTP: 123 alive / 80 gold
- HTTPS: 68 alive / 32 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44583
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
