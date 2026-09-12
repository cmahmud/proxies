# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 454
- HTTP: 122 alive / 95 gold
- HTTPS: 53 alive / 32 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 182 alive / 169 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49318
- Ever gold: 1576

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
