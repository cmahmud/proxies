# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 385
- HTTP: 110 alive / 60 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 164 alive / 152 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33414
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
