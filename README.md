# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 446
- HTTP: 98 alive / 73 gold
- HTTPS: 111 alive / 32 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 190 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47405
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
