# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 384
- HTTP: 107 alive / 59 gold
- HTTPS: 47 alive / 14 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 181 alive / 160 gold

## Historical pool

- Discovered: 178727
- Ever alive: 33414
- Ever gold: 1236

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
