# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 450
- HTTP: 94 alive / 77 gold
- HTTPS: 102 alive / 34 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 191 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47392
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
