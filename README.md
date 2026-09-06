# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 399
- HTTP: 91 alive / 65 gold
- HTTPS: 42 alive / 17 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 186 alive / 162 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48143
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
