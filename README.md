# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 462
- HTTP: 146 alive / 93 gold
- HTTPS: 122 alive / 35 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46871
- Ever gold: 1452

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
