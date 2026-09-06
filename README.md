# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 390
- HTTP: 106 alive / 69 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 171 alive / 153 gold
- SOCKS5: 175 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48169
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
