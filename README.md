# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 408
- HTTP: 113 alive / 61 gold
- HTTPS: 172 alive / 16 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 197 alive / 172 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40737
- Ever gold: 1311

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
