# SyndProxy validated proxy pool

## Current pool

- Alive now: 682
- Gold now: 455
- HTTP: 166 alive / 88 gold
- HTTPS: 101 alive / 30 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 237 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45342
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
