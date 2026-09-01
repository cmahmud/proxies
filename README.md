# SyndProxy validated proxy pool

## Current pool

- Alive now: 631
- Gold now: 455
- HTTP: 138 alive / 84 gold
- HTTPS: 123 alive / 36 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 199 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46833
- Ever gold: 1451

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
