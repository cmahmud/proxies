# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 443
- HTTP: 92 alive / 71 gold
- HTTPS: 97 alive / 30 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 187 alive / 179 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47459
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
