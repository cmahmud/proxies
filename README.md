# SyndProxy validated proxy pool

## Current pool

- Alive now: 688
- Gold now: 462
- HTTP: 144 alive / 94 gold
- HTTPS: 134 alive / 30 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 237 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46251
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
