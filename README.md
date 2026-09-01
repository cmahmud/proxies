# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 425
- HTTP: 87 alive / 69 gold
- HTTPS: 105 alive / 30 gold
- SOCKS4: 176 alive / 157 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47288
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
