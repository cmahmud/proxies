# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 464
- HTTP: 130 alive / 92 gold
- HTTPS: 126 alive / 34 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 229 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45753
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
