# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 436
- HTTP: 111 alive / 87 gold
- HTTPS: 57 alive / 29 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 185 alive / 164 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49433
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
