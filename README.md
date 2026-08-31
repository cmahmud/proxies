# SyndProxy validated proxy pool

## Current pool

- Alive now: 685
- Gold now: 467
- HTTP: 143 alive / 97 gold
- HTTPS: 135 alive / 32 gold
- SOCKS4: 176 alive / 163 gold
- SOCKS5: 231 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46238
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
