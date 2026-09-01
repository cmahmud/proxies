# SyndProxy validated proxy pool

## Current pool

- Alive now: 625
- Gold now: 464
- HTTP: 142 alive / 93 gold
- HTTPS: 116 alive / 36 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 190 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46878
- Ever gold: 1455

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
