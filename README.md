# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 464
- HTTP: 126 alive / 90 gold
- HTTPS: 128 alive / 32 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 218 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45943
- Ever gold: 1438

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
