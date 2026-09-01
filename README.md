# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 470
- HTTP: 130 alive / 95 gold
- HTTPS: 111 alive / 37 gold
- SOCKS4: 173 alive / 163 gold
- SOCKS5: 195 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46883
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
