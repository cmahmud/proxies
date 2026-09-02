# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 443
- HTTP: 134 alive / 79 gold
- HTTPS: 117 alive / 25 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47650
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
