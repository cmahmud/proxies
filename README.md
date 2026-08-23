# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 197
- HTTP: 163 alive / 43 gold
- HTTPS: 42 alive / 8 gold
- SOCKS4: 134 alive / 64 gold
- SOCKS5: 155 alive / 82 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32728
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
