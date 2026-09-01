# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 458
- HTTP: 125 alive / 83 gold
- HTTPS: 115 alive / 36 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 186 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46706
- Ever gold: 1446

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
