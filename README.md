# SyndProxy validated proxy pool

## Current pool

- Alive now: 707
- Gold now: 458
- HTTP: 148 alive / 92 gold
- HTTPS: 155 alive / 32 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 228 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46087
- Ever gold: 1440

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
