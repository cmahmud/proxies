# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 437
- HTTP: 135 alive / 74 gold
- HTTPS: 113 alive / 28 gold
- SOCKS4: 187 alive / 164 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47643
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
