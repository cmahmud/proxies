# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 393
- HTTP: 104 alive / 71 gold
- HTTPS: 40 alive / 15 gold
- SOCKS4: 173 alive / 152 gold
- SOCKS5: 175 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48169
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
