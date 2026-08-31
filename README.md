# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 456
- HTTP: 116 alive / 89 gold
- HTTPS: 117 alive / 33 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45658
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
