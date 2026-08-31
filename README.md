# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 480
- HTTP: 145 alive / 99 gold
- HTTPS: 128 alive / 43 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45099
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
