# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 455
- HTTP: 118 alive / 87 gold
- HTTPS: 119 alive / 32 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46715
- Ever gold: 1447

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
