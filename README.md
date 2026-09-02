# SyndProxy validated proxy pool

## Current pool

- Alive now: 633
- Gold now: 440
- HTTP: 135 alive / 76 gold
- HTTPS: 124 alive / 26 gold
- SOCKS4: 188 alive / 163 gold
- SOCKS5: 186 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47618
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
