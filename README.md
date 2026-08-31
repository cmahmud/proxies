# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 464
- HTTP: 146 alive / 95 gold
- HTTPS: 137 alive / 31 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 236 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46248
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
