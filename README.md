# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 443
- HTTP: 137 alive / 78 gold
- HTTPS: 116 alive / 29 gold
- SOCKS4: 186 alive / 165 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47640
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
